# 📘 Assignment: Search & Sort Challenges

## 🎯 Objective

Students will implement basic search and sorting algorithms, compare their correctness and performance on different input sizes, and justify which algorithm to use in each scenario.

## 📝 Tasks

### 🛠️ Implement search algorithms

#### Description
Implement `linear_search` and `binary_search` as Python functions. Ensure `binary_search` assumes a sorted input.

#### Requirements
Completed program should:

- Provide `linear_search(arr, target)` returning the index or -1
- Provide `binary_search(arr, target)` returning the index or -1
- Include brief docstrings explaining complexity and preconditions


### 🛠️ Implement sorting algorithms

#### Description
Implement `bubble_sort` and `merge_sort` so students can compare simple and efficient sorting strategies.

#### Requirements
Completed program should:

- Provide `bubble_sort(arr)` and `merge_sort(arr)` returning new sorted lists
- Not mutate the original input (return a new list)


### 🛠️ Compare runtime and justify choices

#### Description
Run simple benchmarks on varying input sizes (small, medium, large) and record the observed runtimes. Based on results, write 3–4 sentences justifying which algorithms suit which situations.

#### Requirements
Completed program should:

- Include a `run_benchmarks()` helper demonstrating timings
- Contain a short written justification section (in the README or printed by the script)


### Submission

- Submit the `starter-code.py` with implementations and any tests you added.
- Optionally include sample input files or timing outputs.
