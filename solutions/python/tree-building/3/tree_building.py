from dataclasses import dataclass

@dataclass
class Record:
    """A record, with a unique id and the id of the parent record."""
    record_id: int
    parent_id: int


class Node:
    """Create a node with a list of children.
    
    node_id: an int number representing the identity of the node."""
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def records_validation(records):
    """Validate a list of records based on strict integrity constraints.

    This function perform the following safety checks to ensure a valid tree structure can be built:
    1. IDs must be continous integers from 0 to len(records) - 1.
    2. A child ID must be higher than its parent ID.
    3. Only the root record (ID 0) can have a parent ID equal to its own ID.

    Args:
        records (list): a list of Record objects, containing record_id and parent_id attributes. 

    Raises:
        ValueError: If IDs are dicontinuous, out of bounds, or if any record violates the hierarchical tree rules.
     """
    # IDs validation - Continue values starting from 0.
    if records[0].record_id != 0 or len(records) -1 != records[-1].record_id:
        raise ValueError("Record id is invalid or out of order.")

    # Validations for internal consistency
    if any(record.record_id != 0 and record.record_id == record.parent_id for record in records):
            raise ValueError("Only root should have equal record and parent id.")

    if any(record.parent_id > record.record_id for record in records):
        raise ValueError("Node parent_id should be smaller than its record_id.")


def BuildTree(records):
    """Build a tree from a list of records and return its root node.

    Sort and validate the incoming records, instantiate all tree nodes, 
    establish the parent-child connections, and return the root of the 
    constructed tree.

    Args:
        records(list[Record]): A list of Record instances to process.
    Returns:
        Node | None: The root node of the tree, or None if records is empty."""
    if not records:
        return None
    
    # Sort the records according to their IDs
    records.sort(key=lambda x: x.record_id)
    records_validation(records)

    # Create all the nodes
    nodes = {record.record_id: Node(record.record_id) for record in records} # key:node_id, value:Node instance
    root_node = nodes[0]

    # Building the tree
    for record in records[1:]:
        nodes[record.parent_id].children.append(nodes[record.record_id])

    return root_node