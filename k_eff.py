import csv
from collections import defaultdict

## to calculate the effective thermal conductivity, the input csv should be like this

# name,layer,thermal_conductivity_x(W/mK),thermal_conductivity_z(W/mK),thickness(mm),ratio
# Fr4,Layer1,0.35,0.35,0.0008,1
# Cu,Layer1,387,387,0.0008,0.0
# Fr4,Layer2,0.35,0.35,0.0008,0.7
# Cu,Layer2,387,387,0.0008,0.3
# Fr4,Layer3,0.35,0.35,0.0008,1

def read_material_data(csv_file):
    materials = defaultdict(list)
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            materials[row['layer']].append({
                'name': row['name'],
                'thermal_conductivity_x': float(row['thermal_conductivity_x']),
                'thermal_conductivity_z': float(row['thermal_conductivity_z']),
                'thickness': float(row['thickness']) / 1000,  # Convert from mm to m
                'ratio': float(row['ratio'])
            })
    return materials

def calculate_equivalent_conductivities(materials):
    in_plane_resistance = 0
    thru_plane_resistance = 0
    total_thickness = 0
    
    for layer, components in materials.items():
        layer_in_plane_resistance = 0
        layer_thru_plane_resistance = 0
        layer_thickness = 0
        
        for component in components:
            layer_in_plane_resistance += component['ratio'] * (component['thickness'] * component['thermal_conductivity_x'])
            layer_thru_plane_resistance += component['ratio'] / (component['thickness'] / component['thermal_conductivity_z'])
            layer_thickness = max(layer_thickness, component['thickness'])
        
        layer_thru_plane_resistance = 1 / layer_thru_plane_resistance
        thru_plane_resistance += layer_thru_plane_resistance
        in_plane_resistance += layer_in_plane_resistance
        total_thickness += layer_thickness
    
    in_plane_conductivity = in_plane_resistance / total_thickness
    thru_plane_conductivity = total_thickness / thru_plane_resistance
    
    return in_plane_conductivity, thru_plane_conductivity

def main():
    csv_file = input("Enter the path to your CSV file: ")
    materials = read_material_data(csv_file)
    in_plane, thru_plane = calculate_equivalent_conductivities(materials)
    
    print(f"Equivalent in-plane thermal conductivity: {in_plane:.2f} W/(m*K)")
    print(f"Equivalent thru-plane thermal conductivity: {thru_plane:.2f} W/(m*K)")

if __name__ == "__main__":
    main()


