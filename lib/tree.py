class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit = [self.root]
    
    while nodes_to_visit:
      node = nodes_to_visit.pop()
      if(node['id'] == id):
        return node
      else:
        nodes_to_visit = node['children'] + nodes_to_visit