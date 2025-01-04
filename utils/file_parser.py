```python
import textract

def parse_file(filepath):
    try:
        text = textract.process(filepath).decode("utf-8")
        return {"text": text}
    except Exception as e:
        print(f"Error parsing file: {e}")
        return {}
```
