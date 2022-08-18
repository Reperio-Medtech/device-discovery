# device-discovery

Build the docker image
```json
docker build -t device-discovery .
```
Run the image
```json
docker run --rm -it --net=host -P --name device-discovery device-discovery bash
```
Inside the container run the device discovery method
```json
python3 async_device_discovery.py
```
