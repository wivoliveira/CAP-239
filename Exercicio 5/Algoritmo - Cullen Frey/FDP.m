
i = -1.1;
j = 0.1;
x = -1.1;
A = zeros(200000,1);
B = zeros(200000,1);
counter = 1;

while i <= 5.1
    while j <= 5.1
        while x <= 5.1
            data = gevrnd(i,j,x,1000,1);
            data = data(data < 1000);
            data = data(data > -1000);
            skew = skewness(data);
            skew = skew^2;
            kurt = kurtosis(data);
            A(counter,1) = skew;
            B(counter,1) = kurt;
            counter = counter + 1;
            x = x + 0.1;
        end
        j = j + 0.1;
        x = 0.1;
    end
    i = i + 0.1;
    j = 0.1;
end

to_save = [A, B];

save ('result.txt','to_save', '-ascii')
            
        
    