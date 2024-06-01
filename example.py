from anastruct import SystemElements

ss = SystemElements()

# Barras location = [x1, y1], [x2, y2]
ss.add_element(location=[[0, 0], [0, 2]])  # Barra 1
ss.add_element(location=[[0, 2], [0, 4]])  # Barra 2
ss.add_element(location=[[0, 4], [3, 4]])  # Barra 3
ss.add_element(location=[[3, 4], [4, 4]])  # Barra 4
ss.add_element(location=[[4, 4], [6, 4]])  # Barra 5
ss.add_element(location=[[6, 4], [7, 4]])  # Barra 6

ss.add_internal_hinge(node_id=3)
ss.add_internal_hinge(node_id=5)

ss.add_support_fixed(node_id=1)
ss.add_support_roll(node_id=4)
ss.add_support_roll(node_id=6)

ss.point_load(node_id=2,Fx=+5)
ss.q_load(q=-2,element_id=3)
ss.q_load(q=-2,element_id=4)
ss.point_load(node_id=7,Fy=-10)

ss.solve()

ss.show_results()

exit()

ss.show_reaction_force()

ss.show_bending_moment()

ss.show_shear_force()

ss.show_axial_force()
