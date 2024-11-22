# Introduction to HTML

## What is HTML?
- HTML stands for **Hyper Text Markup Language**.
- It is the standard markup language for creating web pages.
- Describes the structure of web pages using markup.
- HTML elements are the building blocks of HTML pages, represented by **tags**.
- Browsers read HTML documents and use these tags to render the page content.
- HTML files have a `.html` or `.htm` file extension.

## HTML Versions
| Version               | Year    |
|-----------------------|---------|
| HTML                  | 1991    |
| HTML 2.0              | 1995    |
| HTML 3.2              | 1997    |
| HTML 4.01             | 1999    |
| HTML 5.0              | 2014    |
| HTML 5.1              | 2016    |
| HTML 5.1 (2nd Edition)| 2017    |
| HTML 5.2              | 2017    |

## HTML Tags
- HTML tags are surrounded by angle brackets `< >`.
- They usually come in pairs: an opening tag `<tag>` and a closing tag `</tag>`.
- HTML tags are not case sensitive (e.g., `<p>` is the same as `<P>`).
- Content between the tags is the element content.

## HTML Elements
- An **HTML element** includes the opening tag, content, and closing tag.
  - **Opening Tag**: Indicates the start of an element.
  - **Closing Tag**: Indicates the end of an element (preceded by `/`).
  - **Content**: Text, other elements, or both.

### Example:
```html
<p>This is a paragraph.</p>
```

## Empty HTML Elements
- HTML elements with no content are called empty elements.
- Example: <br> (line break) is an empty element without a closing tag.

## HTML Attributes
- Provide additional information about HTML elements.
- Specified in the start tag in name/value pairs, e.g., name="value".
- Attributes should always be enclosed in quotes (double quotes preferred).

## Basic HTML Document Structure
1. **`<!DOCTYPE>` Declaration**:
   - Represents the document type, helping browsers display pages correctly.
   - For HTML5: <!DOCTYPE html>.

2. **`<html>` Element**:
   - The root element containing all other elements.

3. **`<head>` Element**:
   - Contains metadata, styles, scripts, and other non-rendered content.

4. **`<meta>` Element**:
   - Provides metadata like character encoding (UTF-8), author, keywords, etc.

5. **`<title>` Element**:
   - Every document must include a descriptive title within the head section.

6. **`<body>` Element**:
   - Contains all the visible content that appears in the browser window.

### Example of a Basic HTML Document:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>My Web Page</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>This is a simple HTML document.</p>
</body>
</html>
```
### Web Browsers
- Browsers (Chrome, Firefox, Safari, etc.) are used to read HTML documents and display them.
- They do not display HTML tags but use them to render the content on the page.