class Record:
    """A record, with a unique id and the id of the parent record."""
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    """Creates a node with a list of children
    
    node_id: an int number representing the identity of the node."""
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    """Takes a list of records containing ids and partent ids, builds nodes and connect them to generate the tree. Returns the root of the tree.

    Args:
        records(list): a list of elements of the class Record.
    Returns:
        root(Object)"""
    if not records:
        return None
    
    records.sort(key=lambda x: x.record_id)

    # IDs validation - Continue values starting from 0.
    if records[0].record_id != 0 or len(records) -1 != records[-1].record_id:
        raise ValueError("Record id is invalid or out of order.")

    nodes = {}
    root = None
        
    for record in records:
        # Validations for internal consistency
        if record.parent_id > record.record_id:
            raise ValueError("Node parent_id should be smaller than its record_id.")
        
        if record.record_id != 0 and record.record_id == record.parent_id:
            raise ValueError("Only root should have equal record and parent id.")

        # Node creation
        new_node = Node(record.record_id)
        nodes[new_node.node_id] = new_node

        # Nodes conexion
        if record.parent_id == 0 and record.record_id == 0:
            root = new_node
        else:
            nodes[record.parent_id].children.append(new_node)

    return root


# records = [
#             Record(1, 0),
#             Record(2, 0)
#         ]

# print(records)
# arbol = BuildTree(records)
# print(arbol.node_id)