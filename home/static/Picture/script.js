$(document).ready(function () {
    const questions = $('#questions');
    const result = $('#result');
    const csrf = $('input[name=csrfmiddlewaretoken]').val();
    const sendSearchData = _.debounce((query) => {
        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/search_document/',
            data: {
                'csrfmiddlewaretoken': csrf,
                'questions': query,
            },
            success: (res) => {
                const data = res.data;
                if (Array.isArray(data) && data.length > 0) {
                    result.empty();
                    data.forEach((item) => {
                        result.append(`
                      <tr>
                        <td class="text-center">${item.questions}</td>
                        <td class="text-center">${item.answer}</td>
                      </tr>
                    `);
                    });
                } else {
                    if (query.length === 0) {
                        result.empty();
                    } else {
                        result.empty();
                        result.append('<tr><td class="text-center" style="color: red;">Нет такой информации.</td></tr>');
                    }
                }
            },
            error: (err) => {
                console.log(err);
            },
        });
    }, 300);
    questions.on('keyup', function (e) {
        const query = $(this).val();
        if (result.hasClass('not-visible')) {
            result.removeClass('not-visible');
        }
        sendSearchData(query);
    });
});