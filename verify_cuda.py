import torch

# Check if CUDA is available
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"CUDA version: {torch.version.cuda}")
    print(f"Number of CUDA devices: {torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
        print(f"Device {i}: {torch.cuda.get_device_name(i)}")
    
    # Create a small tensor and move it to GPU to verify CUDA works
    x = torch.rand(5, 3)
    print(f"CPU tensor: {x}")
    
    # Move tensor to GPU
    if torch.cuda.is_available():
        x = x.cuda()
        print(f"GPU tensor: {x}")
        
        # Run a small operation to verify computation works
        y = x * 2
        print(f"GPU computation result: {y}")
        print("CUDA is working correctly with PyTorch!")
