#used to set up and run the simulation
import openmc

material = openmc.Material()
material.add_element('U', 1.0)
material.set_density('g/cm3', 10.5)
materials = openmc.Materials([material])
materials.export_to_xml()

#def geometry
sphere = openmc.Sphere(r=50.0, boundary_type = 'vacuum')
cell = openmc.Cell(region = -sphere)
cell.fill = material
geometry = openmc.Geometry([cell])
geometry.export_to_xml()

#def settings
settings = openmc.Settings()
settings.batches = 100
settings.particles = 1000
settings.run_mode = 'fixed source'
settings.esport_to_xml()

openmc.run()