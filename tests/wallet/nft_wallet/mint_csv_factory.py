import asyncio
import csv
from secrets import token_bytes
from typing import Any, List

from faker import Faker

from chia.types.blockchain_format.sized_bytes import bytes32

fake = Faker()
royalty_did = bytes32(token_bytes(32)).hex()


async def create_nft_sample() -> List[Any]:
    sample = [
        fake.image_url(),  # data_url
        bytes32(token_bytes(32)).hex(),  # data_hash
        fake.url(),  # metadata_url
        bytes32(token_bytes(32)).hex(),  # metadata_hash
        fake.url(),  # license_url
        bytes32(token_bytes(32)).hex(),  # license_hash
        1,  # edition_number
        1,  # edition_count
        royalty_did,  # royalty_ph
        bytes32(token_bytes(32)).hex(),  # target ph
    ]
    return sample


async def main() -> None:
    count = 10000
    coros = [create_nft_sample() for _ in range(count)]
    data = await asyncio.gather(*coros)
    with open("sample.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)


if __name__ == "__main__":
    asyncio.run(main())
