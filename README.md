# BasicAccessControlAlgorithm or IP Address Allow List Updater

## Description:

As a security professional working at a health care company, the task is to regularly update a file that identifies employees with access to restricted content. The file is based on the IP addresses of employees working with personal patient records. There are two lists: an allow list for permitted IP addresses and a remove list for employees who must be removed from the allow list.

## Algorithm Steps:

1. **Open the file containing the allow list.**
   - Use the `open()` function with the "r" parameter to open the file.

2. **Read the file contents.**
   - Utilize the `.read()` method to read the contents of the file.

3. **Convert the string into a list.**
   - Use the `.split()` method to convert the string of IP addresses into a list.

4. **Iterate through the remove list.**
   - Use a `for` loop to iterate through the IP addresses in the remove list.

5. **Remove IP addresses that are on the remove list.**
   - Employ the `.remove()` method to eliminate IP addresses from the allow list.

6. **Update the file with the revised list of IP addresses.**
   - Open the file again, this time with the "w" parameter, to overwrite its contents with the updated allow list.

## Usage:

Follow these steps to update the IP address allow list for your health care company.

1. Clone the repository to your local machine.
2. Run the Python script to execute the IP address update algorithm.

## Installation:

Ensure you have Python installed on your machine. No additional dependencies are required.

## Contributors:

- murat akar


Feel free to contribute to this project by submitting pull requests or opening issues.


