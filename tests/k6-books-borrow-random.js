import http from 'k6/http';

export const options = {
    vus: 3,
    iterations: 100000,
};

export default function () {
    const url = 'http://127.0.0.1:1337/book/borrow-random';

    const params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    http.get(url, params);
}