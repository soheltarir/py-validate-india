# py-validate-india
Python module to validate and extract Indian Mobile, Aadhaar, GST, PAN, etc.

## Installation
```sh
pip install validate-india
```

## Validations
Below are the list of documents for which validators are provided in this package:
- Aadhaar
- Mobile Number
- PAN
- GST
- Bank IFSC
- ESIC
- UAN

## Usage

Below is an example of simple validation for mobile numbers

```python
from validate-india import mobile


if __name__ == '__main__':
  if mobile.is_valid('8888899999'):
    print('This is a valid mobile number')
  else:
    print('Invalid mobile number provided')

```

## To-Do List
- [ ] Extract PAN Number, Full Name, Father's Name and Date of Birth from an image using OCR.
- [ ] Extract Aadhaar Number, Full Name, Date of Birth and Gender from Aadhaar Image using OCR.
