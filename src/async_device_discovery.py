import asyncio
import contextlib

from pupil_labs.realtime_api.discovery import Network, discover_devices


async def main():
    async with Network() as network:
        print("Looking for the next best device...\n\t", end="")
        print(await network.wait_for_new_device(timeout_seconds=10))

        print("---")
        print("All devices after searching for additional 5 seconds:")
        await asyncio.sleep(5)
        print(network.devices)


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())