import docker

# Initialize Docker client
client = docker.from_env()

output = client.containers.run("hairyhenderson/figlet", "salut UTM 2024", remove=True)

output = output.decode("utf-8")

print(output)
