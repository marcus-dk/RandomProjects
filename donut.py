import math

# full discretion. this is a port of the donut.c code to python
# i did not by any means write the original nor do i fully understand it
# i simply ported it to python by following my knowledge of python
# that said
# ported by: marcusS 7/01/21

def render_frame(A, B):

    # precompute the sin/cos values of A and B
    cosA = math.cos(A)
    sinA = math.sin(A)
    cosB = math.cos(B)
    sinB = math.sin(B)

    charOutput = []
    zBuffer = []

    for i in range(screen_height + 1):
        charOutput.append([' '] * (screen_width + 0))
        zBuffer.append([0] * (screen_width + 0))

    theta = 0
    while (theta < 2* math.pi):
        theta += thetaSpacing

        # precompute the sin/cos of theta
        costheta = math.cos(theta)
        sintheta = math.sin(theta)

        phi = 0
        while (phi < 2*math.pi):
            phi += phiSpacing

            # precompute sin/cos of phi
            cosphi = math.cos(phi)
            sinphi = math.sin(phi)

            circlex = R2 + R1*costheta
            circley = R1*sintheta

            x = circlex*(cosB*cosphi + sinA*sinB*sinphi) - circley*cosA*sinB
            y = circlex*(sinB*cosphi - sinA*cosB*sinphi) + circley*cosA*cosB
            z = K2 + cosA*circlex*sinphi + circley*sinA
            ooz = 1/z

            xp = int(screen_width/2 + K1*ooz*x)
            yp = int(screen_height/2 - K1*ooz*y)

            L = cosphi*costheta*sinB - cosA*costheta*sinphi - sinA*sintheta + cosB*(cosA*sintheta - costheta*sinA*sinphi)

            if L > 0:

                if ooz > zBuffer[xp][yp]:
                    zBuffer[xp][yp] = ooz
                    luminance_index = L*8

                    charOutput[xp][yp] = '.,-~:;=!*#$@'[int(luminance_index)]

    print('\x1b[H')
    for i in range(screen_height):
        for j in range(screen_width):
            print(charOutput[i][j], end='')
        print()

thetaSpacing = 0.07
phiSpacing = 0.02

R1 = 1
R2 = 2
K2 = 5

screen_width = 35
screen_height = 35

K1 = screen_width*K2*3/(8*(R1+R2))

print('\x1b[2J')
A = 1.0
B = 1.0

for i in range(250):
    render_frame(A, B)
    A += 0.08
    B += 0.03
