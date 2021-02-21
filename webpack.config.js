const path = require('path');

module.exports = {
    entry: './static/src/backup.js',
    output: {
        filename: 'bundle.js',
        publicPath: '/static/shared/js/',
        path: path.resolve(__dirname, 'static/shared/js')
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "script-loader"
                },
            }
        ]
    },
    mode: 'production'
}