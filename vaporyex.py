from vapory import *
from math import pi, sqrt, sin, cos
from random import*
from PIL import Image

def create_3D():
    #image.save("process.png")
    n_boxes=randint(25,34)
    h_boxes=randint(20,30)
    distances  = [1*i for i in range(h_boxes)]
    distances2  = [1*j for j in range(n_boxes)]


#box =Box([0.1*i for i in[0, 0, 0]], [0.8*i for i in[1, 1, 1]], Texture(
#                    Pigment( ImageMap('png', '"cube.png"')),
#                    Finish('ambient', 1.2) ),
#                    'rotate',[45,45,45])

    box= [Box([-0.5+y/4, -0.5+x/4, -0.5],[0.5+y/4,x/4+0.5,0.5],Texture('uv_mapping',
                        Pigment( ImageMap('png', '"process.png"')),
                        Finish('diffuse','albedo', 1.2)),
                        'rotate',[randrange(x,180),randrange(x,35),randrange(x,180)])
                for y in distances
                for x in distances2
                ]



    tt=[Background( "color", [0,0,0] )]


    sun = [LightSource([-1500,2500,-2500], 'color', [1.5,1.5,1.5])]


    scene = Scene( Camera('angle', 75,'location',  [0.7, 2,-6],'rotate',[0,-15,0]),
                      #'look_at', [0.5 , 0.5 , 0.5]),
                   objects = (box+sun+tt),
                   included = ["colors.inc", "textures.inc"],
                   defaults = [Pigment( ImageMap('png', '"cube.png"','once')),Finish( 'ambient', 0.1, 'diffuse', 0.9)] )

    scene.render("twitterimg.png", width=500, height=400, antialiasing=0.000001, quality=9)