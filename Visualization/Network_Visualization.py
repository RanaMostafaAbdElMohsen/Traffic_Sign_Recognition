import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    #input
    to_input( 'sample_img.jpg' ),
    to_Conv("c1", 58, 32, offset="(0,0,0)", to="(0,0,0)", height=32, depth=32, width=4,caption="conv1"),
    to_Conv("c2", 56, 32, offset="(0,0,0)", to="(c1-east)", height=30, depth=30, width=4,caption="conv2" ),
    to_Pool("p1", offset="(0,0,0)", to="(c2-east)", height=26, depth=26, width=1),
    to_Conv("c3", 26, 128, offset="(2,0,0)", to="(p1-east)", height=28, depth=28, width=6,caption="conv3" ),
    to_connection( "p1", "c3"),
    to_Conv("c4", 24, 128, offset="(0,0,0)", to="(c3-east)", height=26, depth=26, width=6, caption="conv4" ),
    to_Pool("p2", offset="(0,0,0)", to="(c4-east)", height=22, depth=22, width=1),
    to_Conv("c5", 10, 256, offset="(2,0,0)", to="(p2-east)", height=20, depth=20, width=8, caption="conv5" ),
    to_connection( "p2", "c5"), 
    to_Conv("c6", 8, 256, offset="(0,0,0)", to="(c5-east)", height=18, depth=18, width=8,caption="conv6" ),
    to_Pool("p3", offset="(0,0,0)", to="(c6-east)", height=14, depth=14, width=1),
    to_ConvSoftMax("fc1", 4096 ,"(2,0,0)", "(p3-east)", width=1.5, height=3, depth=60, caption="Flatten"),
    to_connection( "p3", "fc1"),
    to_SoftMax("fc2", 512 ,"(1.5,0,0)", "(fc1-east)", width=1.5, height=3, depth=40, caption="fc1"),
    to_connection("fc1","fc2"),
    to_SoftMax("soft1", 43 ,"(1.5,0,0)", "(fc2-east)", caption="Softmax", width=1.5, height=3, depth=20),
    to_connection("fc2","soft1"),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()