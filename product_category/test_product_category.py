import unittest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType

from product_category import get_product_category_pairs

class TestProductCategory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up test environment")
        cls.spark = SparkSession.builder.master("local[*]").appName("TestProductCategory").getOrCreate()
        print("Spark session created")

        products_schema = StructType([
            StructField("product_id", StringType(), True),
            StructField("product_name", StringType(), True),
        ])
        categories_schema = StructType([
            StructField("category_id", StringType(), True),
            StructField("category_name", StringType(), True),
        ])
        links_schema = StructType([
            StructField("product_id", StringType(), True),
            StructField("category_id", StringType(), True),
        ])

        cls.products_data = [
            ("p1", "Product 1"),
            ("p2", "Product 2"),
            ("p3", "Product 3"),  # нет категории
        ]
        cls.categories_data = [
            ("c1", "Category 1"),
            ("c2", "Category 2"),
        ]
        cls.links_data = [
            ("p1", "c1"),
            ("p1", "c2"),
            ("p2", "c1"),
        ]

        cls.products_df = cls.spark.createDataFrame(cls.products_data, products_schema)
        cls.categories_df = cls.spark.createDataFrame(cls.categories_data, categories_schema)
        cls.links_df = cls.spark.createDataFrame(cls.links_data, links_schema)

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_correct_pairs(self):
        result_df = get_product_category_pairs(self.products_df, self.categories_df, self.links_df)

        self.assertEqual(
            result_df.filter((col("product_name") == "Product 1") & (col("category_name") == "Category 1")).count(),
            1)

        self.assertEqual(
            result_df.filter((col("product_name") == "Product 1") & (col("category_name") == "Category 2")).count(),
            1)

        self.assertEqual(
            result_df.filter((col("product_name") == "Product 2") & (col("category_name") == "Category 1")).count(),
            1)

    def test_products_without_category(self):
        result_df = get_product_category_pairs(self.products_df, self.categories_df, self.links_df)

        product3_rows = result_df.filter(col("product_name") == "Product 3").collect()
        self.assertEqual(len(product3_rows), 1)
        self.assertIsNone(product3_rows[0]['category_name'])

if __name__ == "__main__":
    unittest.main()
