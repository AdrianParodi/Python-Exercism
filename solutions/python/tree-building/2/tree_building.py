from dataclasses import dataclass

@dataclass
class Record:
    """A record, with a unique id and the id of the parent record."""

    record_id: int
    parent_id: int


class Node:
    """Creates a node with a list of children.
    node_id: an int number representing the identity of the node."""

    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def records_validation(records):
    """Sort and validate a list of records based on strict integrity constraints.

    This function sorts the incoming records by their record_id and perform the following safety checks to ensure a valid tree structure can be built:
    1. IDs must be continous integers from 0 to len(records) - 1.
    2. A child ID must be higher than its parent ID.
    3. Only the root record (ID 0) can have a parent ID equal to its own ID.

    Args:
        records (list): a list of Record objects, containing record_id and parent_id attributes. 

    Raises:
        ValueError: If IDs are dicontinuous, out of bounds, or if any record violates the hierarchical tree rules.
     """
    records.sort(key=lambda x: x.record_id)

    # IDs validation - Continue values starting from 0.
    if records[0].record_id != 0 or len(records) -1 != records[-1].record_id:
        raise ValueError("Record id is invalid or out of order.")

    # Validations for internal consistency
    for record in records:
        if record.parent_id > record.record_id:
            raise ValueError("Node parent_id should be smaller than its record_id.")
        
        if record.record_id != 0 and record.record_id == record.parent_id:
            raise ValueError("Only root should have equal record and parent id.")


def BuildTree(records):
    """Takes a list of records containing ids and partent ids, builds nodes and connect them to generate the tree. Returns the root of the tree.

    Args:
        records(list): a list of elements of the class Record.
    Returns:
        root(Object)"""
    
    if not records:
        return None
    
    records_validation(records)
    
    nodes = {} # key:node_id, value:Node instance

    # Create the root node
    root_node = Node(records[0].record_id)
    nodes[root_node.node_id] = root_node

    # Building the tree
    for record in records[1:]:
        new_node = Node(record.record_id)
        nodes[new_node.node_id] = new_node
        nodes[record.parent_id].children.append(new_node)

    return root_node