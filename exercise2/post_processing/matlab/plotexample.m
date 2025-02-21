%% Load chem1d output data in matrix y
% Variable names are loaded into cell array a
[y,t,a] = readchem1d('yiend.dat');

% Assign some pointers
iTemp = find(strcmpi('temp',a));
iDensity = find(strcmpi('density',a));
iMassFlow = find(strcmpi('massflow',a));
iEnthalpy = find(strcmpi('Enthalpy',a));
iCH4  = find(strcmpi('CH4',a));
iO2   = find(strcmpi('O2',a));
iCO2  = find(strcmpi('CO2',a));
iH2O  = find(strcmpi('H2O',a));
iCO   = find(strcmpi('CO',a));
iNO   = find(strcmpi('NO',a));
iOH   = find(strcmpi('OH',a));
% Add more species here, if you want

% Put spatial coordinate in array x
x = y(:,strcmpi('x(i)',a));
% Put mixture fraction in array Z
Z = y(:,strcmpi('MixFrac',a));

%% Plot T vs x
figure(1);
plot(x, y(:,iTemp), '.-');
xlabel('x [cm]');
ylabel('T [K]');

%% Plot species mass fractions vs x
figure(2);
% Select some species
ivar = [iCH4, iO2, iCO2, iH2O, iCO, iOH];
plot(x, y(:,ivar), '.-');
xlabel('x [cm]');
ylabel('Mass fraction [-]');
% Add a legend
legend(a{ivar});

% Uncomment next line for log scale
% set(gca, 'Yscale', 'log', 'Ylim', [1e-8 1]);

%% Plot NO mass fraction vs x
figure(3);
plot(x, y(:,iNO), '.-');
xlabel('x [cm]');
ylabel('NO mass fraction [-]');


