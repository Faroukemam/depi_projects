import numpy as np

"""
    A class to represent a mathematical vector and perform vector operations.

    Args:
        components (list | tuple): A list or tuple representing the vector components.

    Attributes:
        components (np.ndarray): The components of the vector.

    Methods:
        __init__(components): Initializes the vector with given components.
        __validate_vector(other): Validates if another object is a compatible Vector.
        __add__(other): Adds two vectors.
        __sub__(other): Subtracts two vectors.
        dot(other): Computes the dot product with another vector.
        Magnitude(): Returns the magnitude (length) of the vector.
        ScalarMul(scalar): Multiplies the vector by a scalar.
        Normalize(): Returns the normalized (unit) vector.
        Details(): Returns a string with details about the vector.
        __repr__(): Returns the string representation of the vector.
    Raises:
        TypeError: If the operand is not a Vector or if scalar is not a number.
        ValueError: If vectors are not of the same dimension or if trying to normalize a zero
"""
class Vector:

    def __init__(self, components: list | tuple):
        self.components = np.array(components)
    
    def __validate_vector(self, other: "Vector"):
        if not isinstance(other, Vector):
            raise TypeError("Operand must be a Vector.")
        if self.components.shape != other.components.shape:
            raise ValueError("Vectors must be of the same dimension.")

    def __add__(self, other: "Vector") -> "Vector":
        self.__validate_vector(other)
        return Vector(self.components + other.components)

    def __sub__(self, other: "Vector") -> "Vector":
        self.__validate_vector(other)
        return Vector(self.components - other.components)

    def dot(self, other: "Vector") -> float:
        self.__validate_vector(other)
        return float(np.dot(self.components, other.components))

    def Magnitude(self) -> float:
        return float(np.linalg.norm(self.components))

    def ScalarMul(self, scalar: float) -> "Vector":
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number.")
        return Vector(self.components * scalar)

    def Normalize(self) -> "Vector":
        mag = self.Magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(self.components / mag)
    
    def Details(self):
        return f"{'#'*20}\nVector({self.components.tolist()})\nwith: \nmagnitude {self.Magnitude()}\nnormalized {self.Normalize().components.tolist()}\n{'#'*20}"

    def __repr__(self):
        return f"Vector({self.components})"

"""
    Definition:
        A class for representing and performing operations on mathematical matrices using NumPy arrays.
    Args:
        rows (list | tuple): A 2D array-like structure representing the matrix rows.
    Attributes:
        rows (np.ndarray): The underlying NumPy array storing matrix data.
    Methods:
        __add__(other: "Matrix") -> "Matrix":
            Adds two matrices of the same dimensions and returns a new Matrix.
        __sub__(other: "Matrix") -> "Matrix":
            Subtracts another matrix from this matrix (of the same dimensions) and returns a new Matrix.
        Multiply(other: "Matrix") -> "Matrix":
            Multiplies this matrix by another matrix (if dimensions align) and returns the result as a new Matrix.
        ScalarMul(scalar: float) -> "Matrix":
            Multiplies every element of the matrix by a scalar and returns a new Matrix.
        Transpose() -> "Matrix":
            Returns the transpose of the matrix as a new Matrix.
        Determinant() -> float:
            Computes and returns the determinant of the matrix (only for square matrices).
        Inverse() -> "Matrix":
            Computes and returns the inverse of the matrix (only for non-singular square matrices).
        Details():
            Returns a string with detailed information about the matrix, including its determinant and inverse.
        __repr__():
            Returns a string representation of the Matrix object.
    Raises:
        ValueError: If input is not a 2D array-like structure, or if matrix operations are attempted with incompatible dimensions.
        TypeError: If operands are not Matrix instances or if scalar is not a number.
"""   
class Matrix:

    def __init__(self, rows: list | tuple):
        self.rows = np.array(rows)
        if self.rows.ndim != 2:
            raise ValueError("Input must be a 2D array-like structure.")
    
    def __validate_matrix(self, other: "Matrix"):
        if not isinstance(other, Matrix):
            raise TypeError("Operand must be a Matrix.")
        if self.rows.shape[1] != other.rows.shape[0]:
            raise ValueError("Matrix dimensions do not align for multiplication.")
        
    def __add__(self, other: "Matrix") -> "Matrix":
        self.__validate_matrix(other)  # Corrected the call to the private method
        if self.rows.shape != other.rows.shape:
            raise ValueError("Matrices must be of the same dimensions for addition.")
        return Matrix(self.rows + other.rows)

    def __sub__(self, other: "Matrix") -> "Matrix":
        self.__validate_matrix(other)
        if self.rows.shape != other.rows.shape:
            raise ValueError("Matrices must be of the same dimensions for subtraction.")
        return Matrix(self.rows - other.rows)
    
    def Multiply(self, other: "Matrix") -> "Matrix":
        self.__validate_matrix(other)
        return Matrix(np.dot(self.rows, other.rows))
    
    def ScalarMul(self, scalar: float) -> "Matrix":
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number.")
        return Matrix(self.rows * scalar)
    
    def Transpose(self) -> "Matrix":
        return Matrix(self.rows.T)
    
    def Determinant(self) -> float:
        if self.rows.shape[0] != self.rows.shape[1]:
            raise ValueError("Determinant can only be computed for square matrices.")
        return float(np.linalg.det(self.rows))
    
    def Inverse(self) -> "Matrix":
        if self.rows.shape[0] != self.rows.shape[1]:
            raise ValueError("Inverse can only be computed for square matrices.")
        if np.linalg.det(self.rows) == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        return Matrix(np.linalg.inv(self.rows))
    
    def Details(self):
        return f"{'#'*20}\nMatrix({self.rows.tolist()})\nwith: \ndeterminant {self.Determinant()}\ninverse {self.Inverse().rows.tolist() if self.rows.shape[0] == self.rows.shape[1] else 'N/A'}\n{'#'*20}"

    def __repr__(self):
        return f"Matrix({self.rows.tolist()})"