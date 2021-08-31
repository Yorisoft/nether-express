def getX():
    print('What is yor X coridinate? ')
    x_cord =  float(input())

    return x_cord/8

def getZ():
    print('What is yor Z coridinate? ')
    z_cord =  float(input())

    return z_cord/8

def main():
    x_cord = getX()
    z_cord = getZ()

    print("Build your portal at X:", x_cord, " Z:", z_cord)

if __name__ == "__main__":
    main()