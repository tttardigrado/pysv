from dataclasses import dataclass
from typing import List, Tuple
from pysv.functions.output import error_message, title_message


@dataclass()
class CSVFile:
    """CSV File loaded into memory"""

    header: List[str]  # column names / table header
    rows: List[List[str]]  # rows of he csv file

    def is_loaded(self) -> bool:
        """
        Know if the CSV file has been loaded or if it is empty

        Returns:
            (bool): if the csv file has been loaded
        """
        return bool(self.header and self.rows)

    def add(self, row: List[str]) -> None:
        """Add a new row to the CSV file rows list

        Arguments:
            row (List[str]): list that should be added
        """
        self.rows.append(row)

    def make_table_str(self) -> str:
        table: str = "<table><tr><th>#</th>"
        for head in self.header:
            table += f"<th>{head}</th>"
        table += "</tr>"

        i: int = 0
        for row in self.rows:
            table += f"<tr><td>{i}</td>"
            i += 1
            for value in row:
                table += f"<td>{value}</td>"
            table += "</tr>"
        table += "</table>"
        return table

    def make_row_num_list(self) -> List[str]:
        return [str(num) for num in range(len(self.rows))]

    def list_columns(self) -> str:
        """
        List all Columns on the CSV file.

        Returns:
            (str): the names of every column:
                Columns: Col1 | Col2 | ... | ColN
        """
        return title_message("Columns", " | ".join(self.header))

    def list_rows(self) -> str:
        """
        List the indexes of the rows on the CSV file.

        Returns:
            (str): the indexes of every row:
                Rows: [0, N]
        """
        # number of rows in the csv
        length: int = len(self.rows)

        if length == 0:
            return error_message("There are no rows!")
        elif length == 1:
            # there's only onw row of index 0
            return title_message("Rows", "0")
        else:
            # there are more than 1 rows
            return title_message("Rows", f"[0, {len(self.rows)-1}]")

    def list_col_and_rows(self) -> str:
        """
        Perform both self.list_rows and self.list_columns

        Returns:
            (str): every column and every row
        """
        return self.list_rows() + "\n" + self.list_columns()

    def peek_column(self, column: str) -> str:
        """
        Get the values on a specified column

        Arguments:
            column (str): Name of the column that should be peeked at

        Returns:
            (str):
                -> error -> Error saying that the column was not found
                -> sucess -> The values of the column in every row

        """
        try:
            # get the index of the column in the header
            index: int = self.header.index(column)

            # list comprehension to get all the values in that column
            values: List[str] = [row[index] for row in self.rows]

            # create the message
            message: str = ""
            for i in range(len(values)):
                message += f"\n«{i}:» {values[i]}"

            # send sucess message
            return title_message(column.capitalize(), message)

        except (ValueError, IndexError):
            return error_message(f"The column «{column}» doesn't exist!")

    def peek_row(self, row: str) -> str:
        """
        Get the values on a specified row

        Arguments:
            row (str): index of the row

        Returns:
            (str):
                -> error -> Error saying that the row was not found
                -> sucess -> Every value in the row
        """

        try:
            # get the index of the row
            row_number: int = int(row)

            # the row that should be peeked
            p_row: List[str] = self.rows[row_number]

            # create Message
            message: str = ""
            for i in range(len(p_row)):
                message += f"\n«{self.header[i]}:» {p_row[i]}"

            # send sucess message
            return title_message(row, message)

        except (ValueError, IndexError):
            return error_message(f"The row «{row}» does not exist!")

    def delete_column(self, column: str) -> str:
        """
        Delete the specified column from the csv file.

        | # | C1 | C2 | C3 | C4 | -> del C2 -> | # | C1 | - | C3 | C4 |
        | 0 | a1 | a2 | a3 | a4 | -> del C2 -> | 0 | a1 | - | a3 | a4 |
        | 1 | b1 | b2 | b3 | b4 | -> del C2 -> | 1 | b1 | - | b3 | b4 |
        | 2 | c1 | c2 | c3 | c4 | -> del C2 -> | 2 | c1 | - | c3 | c4 |
        | 3 | d1 | d2 | d3 | d4 | -> del C2 -> | 3 | d1 | - | d3 | d4 |

        Arguments:
            row (str): the index of the row that should be deleted

        Returns:
            (str):
                -> error -> Error saying that the row was not found
                -> sucess -> Message saying that the row was deleted
        """
        if not column:
            raise IndexError
        try:
            # get the index of the column in the header
            index: int = self.header.index(column)
            del self.header[index]

            # loop through the rows
            for row in self.rows:
                # delete the cell where thw column and the current row meet
                del row[index]

            # send success message
            return title_message(
                "Deleted", f"The column «{column}» was successfully deleted!"
            )

        except (ValueError, IndexError):
            return error_message(f"The column «{column}» does not exist!")

    def delete_row(self, row: str) -> str:
        """
        Delete the specified row from the csv file.

        | # | C1 | C2 | C3 | C4 | -> del 0 -> | # | C1 | C2 | C3 | C4 |
        | 0 | a1 | a2 | a3 | a4 | -> del 0 -> - - - -- - -- - -- - -- -
        | 1 | b1 | b2 | b3 | b4 | -> del 0 -> | 0 | b1 | b2 | b3 | b4 |
        | 2 | c1 | c2 | c3 | c4 | -> del 0 -> | 1 | c1 | c2 | c3 | c4 |
        | 3 | d1 | d2 | d3 | d4 | -> del 0 -> | 2 | d1 | d2 | d3 | d4 |

        Arguments:
            row (str): the index of the row that should be deleted

        Returns:
            (str):
                -> error -> Error saying that the row was not found
                -> sucess -> Message saying that the row was deleted
        """
        if not row:
            raise IndexError
        try:
            # get the index of the row
            index: int = int(row)

            # delete the row
            del self.rows[index]

            # send success message
            return title_message(
                "Deleted", f"The row «{row}» was successfully deleted!"
            )

        except (ValueError, IndexError):
            return error_message(f"The row «{row}» does not exist!")

    def switch_row(self, row1: str, row2: str) -> str:
        """
        Switch the values of one row with another row

        | # | C1 | C2 | C3 | C4 | -> 0->3 -> | # | C1 | C2 | C3 | C4 |
        | 0 | a1 | a2 | a3 | a4 | -> 0->3 -> | 3 | d1 | d2 | d3 | d4 |
        | 1 | b1 | b2 | b3 | b4 | -> 0->3 -> | 1 | b1 | b2 | b3 | b4 |
        | 2 | c1 | c2 | c3 | c4 | -> 0->3 -> | 2 | c1 | c2 | c3 | c4 |
        | 3 | d1 | d2 | d3 | d4 | -> 0->3 -> | 0 | a1 | a2 | a3 | a4 |

        Arguments:
            row1 (str): The first row that should be switched
            row2 (str): The second row that should be switched

        Returns:
            (str):
                -> error -> Error saying one of the rows was not found
                -> sucess -> Message saying that the rows were switched
        """

        try:
            # index of the first row
            ind1: int = int(row1)

            # index of the second row
            ind2: int = int(row2)

            # switch the first row with the second row
            self.rows[ind1], self.rows[ind2] = self.rows[ind2], self.rows[ind1]

            # send success message
            return title_message(
                "Switched",
                f"The rows «{row1}» and «{row2}» were successfully switched!",
            )

        except IndexError:
            return error_message(
                f"At least one of «row {row1}» and «row {row2} do not exist!"
            )

    def switch_column(self, col1: str, col2: str) -> str:
        """
        Switch the values of one column with another column

        | # | C1 | C2 | C3 | C4 | -> C1->C3 -> | # | C1 | C2 | C3 | C4 |
        | 0 | a1 | a2 | a3 | a4 | -> C1->C3 -> | 0 | a3 | a2 | a1 | a4 |
        | 1 | b1 | b2 | b3 | b4 | -> C1->C3 -> | 1 | b3 | b2 | b1 | b4 |
        | 2 | c1 | c2 | c3 | c4 | -> C1->C3 -> | 2 | c3 | c2 | c1 | c4 |
        | 3 | d1 | d2 | d3 | d4 | -> C1->C3 -> | 3 | d3 | d2 | d1 | d4 |

        Arguments:
            col1 (str): The first column that should be switched
            col2 (str): The second column that should be switched

        Returns:
            (str):
                -> error -> Error saying one of the columns was not found
                -> sucess -> Message saying that the columns were switched
        """
        try:
            # index of the first column in the header
            ind1: int = self.header.index(col1)

            # index of the second column in the header
            ind2: int = self.header.index(col2)

            # loop through every row
            for row in self.rows:
                # switch the columns in each row
                row[ind1], row[ind2] = row[ind2], row[ind1]

            # send success message
            return title_message(
                "Switched",
                f"The columns «{col1}» and «{col2}» were successfully switched!",
            )

        except (ValueError, IndexError):
            return error_message(
                f"At least one of «column {col1}» and «column {col2}» do not exist!"
            )

    def get_cell(self, column: str, row: str) -> Tuple[str, str]:
        """
        Get the value of a ceratin cell

        Arguments:
            column (str): the name of the cell's column
            row (str): the index of the cell's row

        Returns:
            (Tuple[str,str]): message and content.
            if there's an error, the content is ""
        """
        if not (column or row):
            raise IndexError

        try:
            # index of the column
            col_index: int = self.header.index(column)
            # index of the row
            row_index: int = int(row)

            # get the value of the cell
            value: str = self.rows[row_index][col_index]

            return (title_message(f"Cell {column}-{row}", value), value)

        except (ValueError, IndexError):
            return (
                error_message(
                    f"At least one of «column {column}» and «row {row}» do not exist!"
                ),
                "",
            )

    def set_cell(self, col: str, row: str, content: str) -> str:
        """
        Set the content of the specified cell

        Arguments:
            col (str): name of the cell's column
            row (str): number of the cell's row
            value (str): value that the cell should be set to

        Returns:
            (str): Message that says if there was an error or the cell was set
        """
        if not (col or row or content):
            return error_message("It's not possible to set that cell")

        try:
            # index of the column
            col_index: int = self.header.index(col)
            # index of the row
            row_index: int = int(row)

            self.rows[row_index][col_index] = content
            return title_message(
                "Set", f"The cell «{col} - {row}» was set to {content}"
            )

        except (ValueError, IndexError):
            # a ValueError means that the column does not exist
            # an Index Error means that the row does not exist
            return error_message("It's not possible to set that cell")
