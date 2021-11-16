import math

class Volume:

    # Cube
    def cube(self, edge):
        if (not type(edge) is int) and (not type(edge) is float):
            raise Exception('Only int or float allowed')

        if (edge <= 0):
            raise Exception('Edge should be greater than zero')

        return round(edge*edge*edge, 4)


    # Cuboid
    def cuboid(self, length, width, height):
        if (((not type(length) is int) and (not type(length) is float)) or 
            ((not type(width) is int) and (not type(width)) is float) or
            ((not type(height) is int) and (not type(height)))):

            raise Exception('Only int or float allowed')

        if (length <= 0):
            raise Exception('Length should be greater than zero')

        if (width <= 0):
            raise Exception('Width should be greater than zero')

        if (height <= 0):
            raise Exception('Height should be greater than zero')

        return round(length*height*width, 4)


    # Cylinder
    def cylinder(self, radius, height):
        if (((not type(radius) is int) and (not type(radius) is float)) or 
            ((not type(height) is int) and (not type(height)) is float)):
            
            raise Exception('Only int or float allowed')

        if (radius <= 0):
            raise Exception('Radius should be greater than zero')

        if (height <= 0):
            raise Exception('Height should be greater than zero')

        return round(math.pi*radius*radius*height, 4)

    # Sphere
    def sphere(self, radius):
        if (not type(radius) is int) and (not type(radius) is float):
            raise Exception('Only int or float allowed')

        if (radius <= 0):
            raise Exception('Radius should be greater than zero')

        return round(4*math.pi*radius*radius*radius/3, 4)



        

         