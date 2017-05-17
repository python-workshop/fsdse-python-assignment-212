# Given a list of ints, find the products of every other int for each index.

For eg

        None -> TypeError
        [] -> []
        [0] -> []
        [0, 1] -> [1, 0]
        [0, 1, 2] -> [2, 0, 0]
        [1, 2, 3, 4] -> [24, 12, 8, 6]

## Constraints
* Can we use division?
    * No
* Is the output a list of ints?
    * Yes
* Can we assume the inputs are valid?
    * No
* Can we assume this fits memory?
    * Yes