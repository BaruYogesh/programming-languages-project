:- use_module(library(http/http_client)).

auth(Request) :-

  http_post([protocol(http),
    host(localhost),
    port(3001),
    path('/get')],
    form_data([name=baru]),
    Reply,[]).