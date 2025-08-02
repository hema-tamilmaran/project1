import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

export default function LoginScreen({ navigation }) {
  const handleLogin = (role) => {
    if (role === 'farmer') {
      navigation.navigate('FarmerHome');
    } else {
      navigation.navigate('ConsumerHome');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Login As:</Text>
      <Button title="Farmer" onPress={() => handleLogin('farmer')} />
      <View style={{ marginVertical: 10 }} />
      <Button title="Consumer" onPress={() => handleLogin('consumer')} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  title: { fontSize: 24, marginBottom: 20 }
});
import React from 'react';
import { View, Text } from 'react-native';

export default function FarmerHome() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Welcome, Farmer!</Text>
    </View>
  );
}
import React from 'react';
import { View, Text } from 'react-native';

export default function ConsumerHome() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Welcome, Consumer!</Text>
    </View>
  );
}
// App.js
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import LoginScreen from './screens/LoginScreen';
import FarmerHome from './screens/FarmerHome';
import ConsumerHome from './screens/ConsumerHome';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen name="Login" component={LoginScreen} />
        <Stack.Screen name="FarmerHome" component={FarmerHome} />
        <Stack.Screen name="ConsumerHome" component={ConsumerHome} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
