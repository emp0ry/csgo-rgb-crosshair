import telnetlib
import colorsys
import time

def generate_gradient(num_steps):
    colors = []
    for i in range(num_steps):
        # Calculate the normalized value based on the current step
        value = i / (num_steps - 1)
        
        # Convert the normalized value to RGB using the colorsys module
        rgb = colorsys.hsv_to_rgb(value, 1, 1)  # Convert HSV to RGB
        
        # Scale the RGB values to the range 0-255 and convert them to integers
        r = int(rgb[0] * 255)
        g = int(rgb[1] * 255)
        b = int(rgb[2] * 255)
        
        # Append the RGB color to the list
        colors.append((r, g, b))
    return colors

def main():
    try:
        tn = telnetlib.Telnet('127.0.0.1', 2121)

        tn.write('cl_crosshaircolor 5 \n'.encode('utf-8'))
        while True:
            gradient = generate_gradient(500)
            for color in gradient:
                print("R:", color[0], "G:", color[1], "B:", color[2], "Alpha:")
                tn.write(f'cl_crosshaircolor_r {color[0]}; cl_crosshaircolor_g {color[1]}; cl_crosshaircolor_b {color[2]} \n'.encode('utf-8'))
                time.sleep(0.01)
    except:
        print(f"failed to connect to csgo (game not open? -netconport 2121 not set?)")
        time.sleep(1)

if __name__ == '__main__':
    print('''
█▀█ █▀▀ █▄▄   █▀▀ █▀█ █▀█ █▀ █▀ █░█ ▄▀█ █ █▀█
█▀▄ █▄█ █▄█   █▄▄ █▀▄ █▄█ ▄█ ▄█ █▀█ █▀█ █ █▀▄

█▄▄ █▄█   █▀▀ █▀▄▀█ █▀█ █▀█ █▀█ █▄█
█▄█ ░█░   ██▄ █░▀░█ █▀▀ █▄█ █▀▄ ░█░
https://github.com/emp0ry/''')
    main()