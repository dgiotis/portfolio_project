/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../main/templates/main/*.html', // scans all HTML files in your main app
    '../main/**/*.py',             // optional if you use template tags in Python
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
