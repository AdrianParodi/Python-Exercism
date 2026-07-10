"""Module containing a class to simulate a garden with plants assigned to different students."""

class Garden:
    """Creates a garden, with plants assigned to students. Each student has 4 plants, ordered in two rows."""

    plant_types = {"C":"Clover", "G":"Grass", "R":"Radishes", "V":"Violets"}

    def __init__(self, diagram, students=None):
        """init the garden  with a diagram of plants in two rows and the list of students.
        Args:
            diagram (str): a two-line string, representing all the plants in the garden. Each student has 2 plants in each line (total of 4 plants per student).
        Returns:
            None
        """
        if students is None:
            self.students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid','Larry']
        else:
            self.students = sorted(students)

        self.plants_diagram = diagram.split("\n")
    
    def plants(self, student):
        """Method that returns the plants belonging to one particular student.
        Args:
            student(str): the name of the student.
        Returns:
            list: the list of the plants of the student."""
        index_student = self.students.index(student)
        
        # Recover the chars corresponding to the student
        student_plants_raw = self.plants_diagram[0][2*index_student:2*index_student+2] + self.plants_diagram[1][2*index_student:2*index_student+2]

        student_plants = []
        for plant_code in student_plants_raw:
            student_plants.append(Garden.plant_types[plant_code])

        return student_plants
    

jardin = Garden("RC\nGG")