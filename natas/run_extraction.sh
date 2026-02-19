#!/bin/bash
cd /home/gagan/Desktop/ctfs/wargames/natas
python3 solve17.py 2>&1 | tee /tmp/extraction_output.txt
echo "Done! Extraction complete."
tail -5 /tmp/extraction_output.txt
