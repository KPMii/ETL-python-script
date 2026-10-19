from etl.extract import extract_product, extract_users
from etl.transform import transform_product, transfrom_user
from etl.load import load_to_postgres

def run_pipeline():
    print('Starting pipeline')

    product_df = extract_product() 
    user_df = extract_users()

    print('Starting transformation')

    product_df = transform_product(product_df)
    user_df = transfrom_user(user_df)

    print('Loading to postgres')

    load_to_postgres(product_df, 'products')
    load_to_postgres(user_df, 'users')

    print('ETL pipeline completed')

if __name__ == '__main__':
    run_pipeline()