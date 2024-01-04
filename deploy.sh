docker build -t wine_app_build .

# use the following line to create a container and connect to bash
# docker run -it -p 8080:8080 wine_app_build /bin/bash
docker run -p 8080:8080 --name wine_app wine_app_build