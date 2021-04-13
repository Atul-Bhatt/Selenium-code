# Using Selenium

- Import selenium webdriver
- Open the browser using driver.get(url)
- Print the title using driver.title
- To quit the browser use driver.quit()
- To quit a single tab use driver.close()

## Access elements on the page

- Keys is used to click on buttons( I think...).

```python
from selenium.webdriver.common.keys import Keys
```

- use find_element_by_blahblah to search elements

```python
search = driver.find_element_by_name("nameofelement")
search.send_keys("input") # giving input to a test field
search.send_keys(Keys.RETURN) # press the submit button ( Not sure...)
```

- wait till an element exists (moving to a next page after you input something)

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try: main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "main"))
            )
except: # or finally
    driver.quit()
```

```python
main = driver.find_element_by_id("main") # root element from which you want other attributes.
print(main.text)
```
