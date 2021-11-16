import prettytable
from volume import Volume
from prettytable import PrettyTable

vol = Volume()
success= '\033[92m'
error= '\033[91m'
normal= '\033[0m'
yellow = '\033[93m'
blue = '\033[94m'

class Test:

    def testCube(self):
        print(yellow + 'Testing cube' + normal)

        table = PrettyTable([blue + 'Input' + normal, blue + 'Output' + normal])

        try:
            v = vol.cube()
            table.add_row(['No arguments', success + 'Volume of cube is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['No arguments', error + str(e) + normal])
        table.add_row(['', ''])
        
        try:
            v = vol.cube(5, 6)
            table.add_row(['Invalid number of arguments', success + 'Volume of cube is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['Invalid number of arguments', error + str(e) + normal])
        table.add_row(['', ''])

        try:
            v = vol.cube('a')
            table.add_row(['Character input', success + 'Volume of cube is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['Character input', error + str(e) + normal])
        table.add_row(['', ''])

        try:
            v = vol.cube(0)
            table.add_row(['Zero input', success + 'Volume of cube is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['Zero input', error + str(e) + normal])
        table.add_row(['', ''])

        try:
            v = vol.cube(-5)
            table.add_row(['Negative input', success + 'Volume of cube is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['Negative input', error + str(e) + normal])
        table.add_row(['', ''])

        try:
            v = vol.cube(5)
            table.add_row(['Valid input', success + 'Volume of cube is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['Valid input', error + str(e) + normal])

        print(table)


    def testCuboid(self):
        print(yellow + 'Testing cuboid' + normal)

        table = PrettyTable([blue + 'Input' + normal, blue + 'Output' + normal])

        try:
            v = vol.cuboid()
            table.add_row(['No arguments', success + 'Volume of cuboid is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['No arguments', error + str(e) + normal])
        table.add_row(['', ''])
        
        try:
            v = vol.cuboid(5, 6, 7, 9)
            table.add_row(['Invalid number of arguments', success + 'Volume of cuboid is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['Invalid number of arguments', error + str(e) + normal])
        table.add_row(['', ''])

        try:
            v = vol.cuboid('a', 'k', '5')
            table.add_row(['Character input', success + 'Volume of cuboid is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['Character input', error + str(e) + normal])
        table.add_row(['', ''])

        try:
            v = vol.cuboid(0, 0, 0)
            table.add_row(['Zero input', success + 'Volume of cuboid is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['Zero input', error + str(e) + normal])
        table.add_row(['', ''])

        try:
            v = vol.cuboid(-5, -2, -7)
            table.add_row(['Negative input', success + 'Volume of cuboid is ' + str(v) + normal])
        except Exception as e:
            table.add_row(['Negative input', error + str(e) + normal])
        table.add_row(['', ''])

        try:
            v = vol.cuboid(5, 4, 3)
            table.add_row(['Valid input', success + 'Volume of cuboid is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['Valid input', error + str(e) + normal])

        print(table)


    def testCylinder(self):
        print(yellow + 'Testing cylinder' + normal)

        table = PrettyTable([blue + 'Input' + normal, blue + 'Output' + normal])

        try:
            v = vol.cylinder()
            table.add_row(['No arguments', success + 'Volume of cylinder is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['No arguments', error + str(e) + normal])
        table.add_row(['', ''])
        
        try:
            v = vol.cylinder(5)
            table.add_row(['Invalid number of arguments', success + 'Volume of cylinder is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['Invalid number of arguments', error + str(e) + normal])
        table.add_row(['', ''])

        try:
            v = vol.cylinder('a', '7')
            table.add_row(['Character input', success + 'Volume of cylinder is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['Character input', error + str(e) + normal])
        table.add_row(['', ''])

        try:
            v = vol.cylinder(0, 0)
            table.add_row(['Zero input', success + 'Volume of cylinder is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['Zero input', error + str(e) + normal])
        table.add_row(['', ''])

        try:
            v = vol.cylinder(-5)
            table.add_row(['Negative input', success + 'Volume of cylinder is ' + str(v) + normal])
        except Exception as e:
            table.add_row(['Negative input', error + str(e) + normal])
        table.add_row(['', ''])

        try:
            v = vol.cylinder(5, 6)
            table.add_row(['Valid input', success + 'Volume of cylinder is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['Valid input', error + str(e) + normal])

        print(table)
    

    def testSphere(self):
        print(yellow + 'Testing sphere' + normal)

        table = PrettyTable([blue + 'Input' + normal, blue + 'Output' + normal])

        try:
            v = vol.sphere()
            table.add_row(['No arguments', success + 'Volume of sphere is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['No arguments', error + str(e) + normal])
        table.add_row(['', ''])
        
        try:
            v = vol.sphere(5, 6)
            table.add_row(['Invalid number of arguments', success + 'Volume of sphere is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['Invalid number of arguments', error + str(e) + normal])
        table.add_row(['', ''])

        try:
            v = vol.sphere('a')
            table.add_row(['Character input', success + 'Volume of sphere is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['Character input', error + str(e) + normal])
        table.add_row(['', ''])

        try:
            v = vol.sphere(0)
            table.add_row(['Zero input', success + 'Volume of sphere is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['Zero input', error + str(e) + normal])
        table.add_row(['', ''])

        try:
            v = vol.sphere(-5)
            table.add_row(['Negative input', success + 'Volume of sphere is ' + str(v) + normal])
        except Exception as e:
            table.add_row(['Negative input', error + str(e) + normal])
        table.add_row(['', ''])

        try:
            v = vol.sphere(5)
            table.add_row(['Valid input', success + 'Volume of sphere is ' + str(v) + normal])

        except Exception as e:
            table.add_row(['Valid input', error + str(e) + normal])

        print(table)

if __name__ == "__main__":

    test = Test()
    inputs = [1, 2, 3, 4, 5, 'a']

    for i in inputs:
        print(yellow + '\n---Menu---' + normal)
        print('1. Cube\n2. Cuboid\n3. Cylinder\n4. Sphere\n')
        print('Enter your choice: ', end='')
        print(i, end='\n\n')

        if i == 1:
            test.testCube()

        elif i == 2:
            test.testCuboid()

        elif i == 3:
            test.testCylinder()

        elif i == 4:
            test.testSphere()

        else:
            print(error + 'Invalid choice, please try again' + normal)
