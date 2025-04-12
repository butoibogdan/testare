import docker

client = docker.from_env()
container = client.containers.run("hello-world")
print(container.decode(" utf-8"))
