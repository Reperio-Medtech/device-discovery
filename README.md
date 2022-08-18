# device-discovery
Building the docker image
```json
docker build -t device-discovery .
```
Running the image
```json
docker run --rm -it --net=host -P device-discovery bash
```
