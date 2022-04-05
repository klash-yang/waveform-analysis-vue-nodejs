// http://eslint.org/docs/user-guide/configuring
// module.exports = {
//   "root": true,
//   extends: [
//     // 'eslint:recommended',
//     'plugin:vue/recommended' // or 'plugin:vue/base'
//   ],
//   rules: {
//     // override/add rules' settings here
//     // 'vue/valid-v-if': 'error'
//   }
// }


module.exports = {
  root: true,
  parser: 'vue-eslint-parser',
  parserOptions: {
    sourceType: "module",
    ecmaVersion: 8,
  },
  env: {
    node: true
  },
  // https://github.com/standard/standard/blob/master/docs/RULES-en.md
  extends: [
    'plugin:vue/recommended',
    'eslint:recommended',
  ],
  // required to lint *.vue files
  plugins: [],
  // add your custom rules here
  'rules': {
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
    'no-console': 'off',
    "no-unused-vars": 'off',
    'valid-typeof': 'off',
    'no-undef': 'off'
  }
}
