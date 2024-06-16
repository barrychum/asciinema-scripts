#!/bin/bash

# Parameters
input_svg="output.svg"
output_svg="modified_output.svg"
new_width="500"

# Extract the top-level width and height from the SVG file using grep and awk
original_width=$(grep -m 1 '<svg' "$input_svg" | awk -F 'width="' '{print $2}' | awk -F '"' '{print $1}')
original_height=$(grep -m 1 '<svg' "$input_svg" | awk -F 'height="' '{print $2}' | awk -F '"' '{print $1}')

# Debugging output to see the extracted width and height
echo "Extracted original width: $original_width"
echo "Extracted original height: $original_height"

# Check if the original dimensions were extracted successfully
if [ -z "$original_width" ] || [ -z "$original_height" ]; then
  echo "Failed to extract original dimensions from the SVG file."
  exit 1
fi

# Calculate the new height to maintain the aspect ratio
aspect_ratio=$(echo "scale=6; $original_height / $original_width" | bc)
new_height=$(echo "scale=6; $new_width * $aspect_ratio" | bc)

# Debugging output to see the calculated aspect ratio and new height
echo "Calculated aspect ratio: $aspect_ratio"
echo "Calculated new height: $new_height"

# Check if the calculations were successful
if [ -z "$aspect_ratio" ] || [ -z "$new_height" ]; then
  echo "Failed to calculate new dimensions."
  exit 1
fi

# Modify the SVG file using sed to update width and height attributes
# Ensure viewBox remains the same to maintain original scaling of content
sed -E "
s/(<svg[^>]* width=\")[0-9.]+(\")/\1$new_width\2/;
s/(<svg[^>]* height=\")[0-9.]+(\")/\1$new_height\2/;
s/(<rect[^>]* width=\")[0-9.]+(\")/\1$new_width\2/;
s/(<rect[^>]* height=\")[0-9.]+(\")/\1$new_height\2/;
" "$input_svg" | sed "s/viewBox=\"[^\"]*\"/viewBox=\"0 0 $original_width $original_height\"/" > "$output_svg"

echo "SVG modified successfully. New dimensions: width=$new_width, height=$new_height"
