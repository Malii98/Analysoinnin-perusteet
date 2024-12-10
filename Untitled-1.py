import kagglehub

# Download latest version
path = kagglehub.dataset_download("piterfm/olympic-games-medals-19862018")

print("Path to dataset files:", path)