from  layout_code_2 import DrawPanel

#no common property here

panel_code = DrawPanel('camera','PROPERTIES','WINDOW','data','Camera')
panel_code.set_file_name('properties_yaf_camera_second.py')


''' each property consists of five parts  - context, name, type, do_implement label'''
    
properties = []

''' common properties '''
properties.append(['scene','camera_type','enum',False,'Yafaray Camera'])
panel_code.add_properties(properties)

panel_code.add_enum_values('camera_type',['Angular','Orthographic','Perspective','Architect'])

''' if false context is scene'''

panel_code.add_enum('camera_type', 'Angular', ['camera','lens','float',True,'Angle'])
panel_code.add_enum('camera_type', 'Angular', ['scene','max_angle','float',False,'Max Angle'])
panel_code.add_enum('camera_type', 'Angular', ['scene','mirrored','bool',False,'Mirrored'])
panel_code.add_enum('camera_type', 'Angular', ['scene','circular','bool',False,'Circular'])

panel_code.add_enum('camera_type', 'Orthographic', ['camera','ortho_scale','float',True,'Scale'])

panel_code.add_enum('camera_type', 'Perspective', ['scene','bokeh_type','enum',False,'Bokeh Type'])
panel_code.add_enum('camera_type', 'Perspective', ['scene','aperture','float',False,'Aperture'])
panel_code.add_enum('camera_type', 'Perspective', ['camera','dof_distance','float',True,'DOF distance'])
panel_code.add_enum('camera_type', 'Perspective', ['scene','bokeh_rotation','float',False,'Bokeh Rotation'])
panel_code.add_enum('camera_type', 'Perspective', ['scene','bokeh_bias','enum',False,'Bokeh Bias'])
panel_code.add_enum('camera_type', 'Perspective', ['camera','lens','float',True,'Focal Length'])

''' default property is in last position '''
panel_code.add_enum_values('bokeh_type',['Disk2','Triangle','Square','Pentagon','Hexagon','Ring','Disk1'])
panel_code.add_enum_values('bokeh_bias',['Uniform','Center','Edge'])


panel_code.add_enum('camera_type', 'Architect', ['scene','bokeh_type','enum',True,'Bokeh Type'])
panel_code.add_enum('camera_type', 'Architect', ['scene','aperture','float',True,'Aperture'])
panel_code.add_enum('camera_type', 'Architect', ['camera','dof_distance','float',True,'DOF distance'])
panel_code.add_enum('camera_type', 'Architect', ['scene','bokeh_rotation','float',True,'Bokeh Rotation'])
panel_code.add_enum('camera_type', 'Architect', ['scene','bokeh_bias','enum',True,'Bokeh Bias'])
panel_code.add_enum('camera_type', 'Architect', ['camera','lens','float',True,'Focal Length'])

panel_code.add_additional_poll_text('context.camera')
panel_code.generate_code()