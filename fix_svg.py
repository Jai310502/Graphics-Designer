def fix_svg(svg_file):
    # Read the SVG file as text
    with open(svg_file, 'r', encoding='utf-8') as f:
        svg_content = f.read()

    # Find the index of the start and end of the image element's xlink:href attribute
    start_index = svg_content.find('xlink:href="') + len('xlink:href="')
    end_index = svg_content.find('"', start_index)

    # Extract the URL from the xlink:href attribute
    url = svg_content[start_index:end_index]

    # Encode '&' characters in URL
    encoded_url = url.replace('&', '&amp;')

    # Replace the original URL with the encoded one in the SVG content
    fixed_svg_content = svg_content[:start_index] + encoded_url + svg_content[end_index:]

    # Write the corrected SVG back to the file
    with open(svg_file, 'w', encoding='utf-8') as f:
        f.write(fixed_svg_content)

# Path to your SVG file
svg_file_path = 'output.svg'

# Call the function to fix the SVG
fix_svg(svg_file_path)
