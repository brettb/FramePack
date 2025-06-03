#!/bin/bash
# Script to run HunyuanVideo demo with SageAttention enabled

# Disable flash-attention to avoid conflicts with SageAttention
export DISABLE_FLASH_ATTN=1

# Run the demo with SageAttention enabled (now default)
python demo_gradio_f1.py
