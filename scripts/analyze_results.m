function analyze_results(filename)
    data = lpad(filename)
    % do sth
    disp('Analyzing MCNP resu...');
    plot(data(:, 1)), data(: 2));
end

% call teh functtion with the path ot the results file
analyze_results('results/output.txt');
