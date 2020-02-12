#Sphere Triangulator - Jake Brown

from math import sqrt

p=(1+sqrt(5))/2 #golden ratio
icos=[(1,p,0),(-1,p,0),(1,-p,0),(-1,-p,0),
      (0,1,p),(0,-1,p),(0,1,-p),(0,-1,-p),
      (p,0,1),(p,0,-1),(-p,0,1),(-p,0,-1)] #icosahedron vertices
rad=sqrt(1+p**2) #radius of sphere that circumscribes the icosahedron

def get_midpoint(adj_point_list,final_list):
    '''
    Finds the midpoint of two vertices
    The vertices must be adjacent
    '''
    for i in range(len(adj_point_list)):
        v1=adj_point_list[i][0]
        v2=adj_point_list[i][1]
        x1=v1[0]
        y1=v1[1]
        z1=v1[2]
        x2=v2[0]
        y2=v2[1]
        z2=v2[2]
        mid_x=(x1+x2)/2
        mid_y=(y1+y2)/2
        mid_z=(z1+z2)/2
        midpoint=(mid_x,mid_y,mid_z)
        final_list.append(midpoint)
    return final_list

def get_adjacent_points(point_list,n_iter):
    '''
    Creates list of paired points, where
    each pair of points is adjacent
    n_iter is the number of iterations
    '''
    adj_points=[]
    for i in range(len(point_list)):
        v1=point_list[i]
        for j in range(i,len(point_list)):
            v2=point_list[j]
            x1=v1[0]
            y1=v1[1]
            z1=v1[2]
            x2=v2[0]
            y2=v2[1]
            z2=v2[2]
            d=sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
            if d==2/(2**n_iter):
                adj_points.append([v1,v2])
    return adj_points

def project(final,radius):
    '''
    Projects the final list of points onto
    the sphere for triangulation
    '''
    sphere_triangulation=[]
    for point in final:
        x=point[0]
        y=point[1]
        z=point[2]
        mag=sqrt(x**2+y**2+z**2)
        sphere_point=(radius*x/mag,radius*y/mag,radius*z/mag)
        sphere_triangulation.append(sphere_point)
    return sphere_triangulation
        
def triangulate_icosahedron(icosahedron,n_iterations):
    '''
    Triangulates the icosahedron
    '''
    for i in range(n_iterations):
        adj=get_adjacent_points(icosahedron,i)
        icosahedron=get_midpoint(adj,icosahedron)
        #print(i+1,':',len(icosahedron))
    return icosahedron

def scale_final_triangulation(sphere_triangulation,desired_radius,used_radius):
    '''
    Scales the points in the generated triangulation to
    the radius specified by the user
    '''
    scaled_sphere_triangulation=[]
    for point in sphere_triangulation:
        x=point[0]
        y=point[1]
        z=point[2]
        scale_factor=desired_radius/used_radius
        scaled_point=(scale_factor*x,scale_factor*y,scale_factor*z)
        scaled_sphere_triangulation.append(scaled_point)
    return scaled_sphere_triangulation

def main():
    n=int(input('How many iterations? '))
    r=float(input('Desired radius? '))
    icos_triangulation=triangulate_icosahedron(icos,n)
    sphere_triangulation=project(icos_triangulation,rad)
    print(sphere_triangulation)
    scaled_triangulation=scale_final_triangulation(sphere_triangulation,r,rad)
    print(scaled_triangulation)

main()
