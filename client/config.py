import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)

DB_PATH: str = data["DB"]["PATH"]
GRPC_URL: str = f'{data["GRPC"]["URL"]}:{data["GRPC"]["PORT"]}'
