/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')
const color = require('tailwindcss/colors')
module.exports = {
  content: [
      './templates/**/*.html',
      './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
  },
  
  plugins: [
    require('flowbite/plugin')
]
}
