from pyspark.sql.functions import col

def get_product_category_pairs(products_df, categories_df, product_category_links_df):
    """
    Возвращает один DataFrame с парами (product_name, category_name).
    Для продуктов без категорий поле category_name будет null.
    """
    joined = products_df.join(product_category_links_df, 'product_id', 'left')
    joined = joined.join(categories_df, 'category_id', 'left')
    result_df = joined.select(col('product_name'), col('category_name'))
    return result_df
