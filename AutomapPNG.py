import bpy
from pathlib import Path
import os

current_directory = bpy.path.abspath("//") 
def has_material(obj):
    """Checks if the given object has any materials assigned."""
    return len(obj.material_slots) > 0

def search_subfolders(root_dir, search_term):
    """
    Searches for files containing the search term in the given root directory and its subfolders.

    Args:
        root_dir (str): The root directory to start the search from.
        search_term (str): The term to search for in file names.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if search_term in filename:
                return(os.path.join(dirpath, filename))

def remove_after_dot(text):
  """Removes characters after the first dot in a string.

  Args:
    text: The input string.

  Returns:
    The modified string, or the original string if no dot is found.
  """
  dot_index = text.find('.')
  if dot_index != -1:
    return text[:dot_index]
  return text

    
for ob in bpy.context.selected_objects:
    if has_material(ob):
        mat = ob.data.materials[0]
        matName = remove_after_dot(mat.name[5:])
        # Enable nodes for the material
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        
        for node in mat.node_tree.nodes:
            # Check if the node is an image node
            if node.type == 'TEX_IMAGE':
                # Remove the node
                mat.node_tree.nodes.remove(node)
        for node in mat.node_tree.nodes:
            if node.type == 'BSDF_PRINCIPLED':
                #set as primary node
                main_mat_node = node
            
        # Create an Image Texture node
        image_texture = nodes.new(type='ShaderNodeTexImage')
        image_texture.location = (-300, 0)
        
        # Set the image path
        image_path = search_subfolders(current_directory, matName)
        if os.path.exists(image_path):
            image_texture.image = bpy.data.images.load(image_path)

        print("Node inputs:", mat.node_tree)
        # Connect the Image Texture to the Base Color of the Principled BSDF
        mat.node_tree.links.new(image_texture.outputs["Color"], main_mat_node.inputs["Base Color"])
        mat.node_tree.links.new(image_texture.outputs["Alpha"], main_mat_node.inputs["Alpha"])

